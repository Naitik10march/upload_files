import dropbox

class TransferData:
     def __init__(self,access_token) :
        self.access_token = access_token

        def upload_file(self,file_from,file_to):
            dbx = dropbox.Dropbox(self.access_token)

            f = open(file_from, 'rb')
            dbx.files_upload(f.read(), file_to)

            def main():
                access_token = 'sl.BGX5mSyhsxKNTAWcRZXpcTV_2Z-XynBLI-X82QOIAD9HE_19kGQXrya9h4e95TVEewiJqkxeOhSxwz7FMpfpDQVbQSaRv75LCNL7kUuYZb1FA5UN_rDittg9N5lmDoeozcSS9hM'
                transferData = TransferData(access_token)

                file_from = input("enter the file path to transfer : ")
                file_to = input("enter the full path to upload dropbox : ")

                transferData.upload_file(file_from, file_to)
                print("file has been uploaded!!!")

                main()
            
        pass