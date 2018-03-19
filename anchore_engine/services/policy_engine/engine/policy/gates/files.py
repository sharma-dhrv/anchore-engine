import re
import stat
from anchore_engine.services.policy_engine.engine.policy.gate import Gate, BaseTrigger
from anchore_engine.services.policy_engine.engine.logs import get_logger
from anchore_engine.services.policy_engine.engine.policy.params import PipeDelimitedStringListParameter, TriggerParameter, TypeValidator
from anchore_engine.db import AnalysisArtifact
log = get_logger()


class ContentMatchTrigger(BaseTrigger):
    __trigger_name__ = 'content_regex_match'
    __description__ = 'Triggers if the content search analyzer has found any matches.  If the parameter is set, then will only trigger against found matches that are also in the FILECHECK_CONTENTMATCH parameter list.  If the parameter is absent or blank, then the trigger will fire if the analyzer found any matches.'

    regex_name = TriggerParameter(validator=TypeValidator('string'), name='regex_name', description='Name of regex from the FILECHECK_CONTENTMATCH parameter list in analyzer configuration',
                                  is_required=True)

    def evaluate(self, image_obj, context):
        match_filter = self.regex_name.value()

        if match_filter:
            match_decoded = match_filter.encode('base64')
        else:
            return

        for thefile, regexps in context.data.get('content_regexp', {}).items():
            thefile = thefile.encode('ascii', errors='replace')
            if not regexps:
                continue
            for regexp in regexps.keys():
                try:
                    regexp_name, theregexp = regexp.decode('base64').split("=", 1)
                except:
                    regexp_name = None
                    theregexp = regexp.decode('base64')

                if not match_filter:
                    self._fire(msg='File content analyzer found regexp match in container: file={} regexp={}'.format(thefile, regexp.decode('base64')))
                elif regexp == match_filter or theregexp == match_decoded:
                    self._fire(msg='File content analyzer found regexp match in container: file={} regexp={}'.format(thefile, regexp.decode('base64')))
                elif regexp_name and regexp_name == match_decoded:
                    self._fire(msg='File content analyzer found regexp match in container: file={} regexp={}'.format(thefile, regexp.decode('base64')))


class FilenameMatchTrigger(BaseTrigger):
    __trigger_name__ = 'name_match'
    __description__ = 'Triggers if a file exists in the container that has a filename that matches the regex'

    regex = TriggerParameter(validator=TypeValidator('string'), name='regex_name', description='Regex to apply to file names for match', is_required=True)

    def evaluate(self, image_obj, context):
        # decode the param regexes from b64
        regex_param = self.regex.value().decode('string_escape')

        files = []
        if hasattr(context, 'data'):
            files = context.data.get('filenames')

        for thefile in files:
            thefile = thefile.encode('ascii', errors='replace')
            if re.match(regex_param, thefile):
                self._fire(msg='Application of regex matched file found in container: file={} regexp={}'.format(thefile, regex_param))


class SuidCheckTrigger(BaseTrigger):
    __trigger_name__ = 'suid_guid_set'
    __description__ = 'Fires for each file found to have suid or sgid set'

    def evaluate(self, image_obj, context):
        if not image_obj.fs:
            return

        files = image_obj.fs.files
        if not files:
            return

        found = filter(lambda x: (int(x[1].get('mode', 0)) & (stat.S_ISUID | stat.S_ISGID)), files.items())
        for path, entry in found:
            self._fire(msg='SUID or SGID found set on file {}. Mode: {}'.format(path, oct(entry.get('mode'))))


class FileCheckGate(Gate):
    __gate_name__ = 'files'
    __description__ = 'Image File Checks'
    __triggers__ = [
        ContentMatchTrigger,
        FilenameMatchTrigger,
        SuidCheckTrigger
    ]

    def prepare_context(self, image_obj, context):
        """
        prepare the context by extracting the file name list once and placing it in the eval context to avoid repeated
        loads from the db. this is an optimization and could removed.

        :param image_obj:
        :param context:
        :return:
        """
        if image_obj.fs:
            extracted_files_json = image_obj.fs.files

            if extracted_files_json:
                context.data['filenames'] = extracted_files_json.keys()

        content_matches = image_obj.analysis_artifacts.filter(AnalysisArtifact.analyzer_id == 'content_search', AnalysisArtifact.analyzer_artifact == 'regexp_matches.all', AnalysisArtifact.analyzer_type == 'base').all()
        matches = {}
        for m in content_matches:
            matches[m.artifact_key] = m.json_value
        context.data['content_regexp'] = matches

        return context
