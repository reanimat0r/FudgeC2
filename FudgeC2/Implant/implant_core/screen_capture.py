import secrets
import base64

from FudgeC2.Storage.settings import Settings

class ScreenCapture:
    type = "SC"
    args = "base64 target file"
    input = "screenshot"

    def process_implant_response(self, data, filepath):
        """print("sub class")
        :param data: Byte encoded file
        :param filepath: The downloaded file path i.e. C:\Windows\System32\drivers\etc\hosts
        :return: None

        File download takes byte encoded data and directly writes it to a randomly named file, returning the
          file location.
        IN DEV:
          Parse filepath for the filename
          Check for file extensions
          Check if the file exists using SHA1
          Check writing to local file succeeds
          Check for filename uniqueness.
        """

        # filename = secrets.token_hex(3)
        # download_file_path = f"{Settings.file_download_folder}downloaded_file_{filename}"
        # with open(download_file_path, 'wb') as file_h:
        #
        #     file_h.write(base64.b64decode(data))
        # return f"File downloaded: {filepath}\nFile saved to {download_file_path}", None

        return "Screen capture: In dev.", None

    def implant_text(self):
        var = '''
function {{ ron.obf_screen_capture }} ($b){
    try {
    # Capture screen to occur here: 
        $Script:tr = "1"
    } catch {
        Script:tr = "0"
    }
}'''
        return var