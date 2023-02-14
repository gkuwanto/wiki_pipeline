import sys
import gdown
file_id = sys.argv[1]
output_file = sys.argv[2]
gdown.download(f"https://drive.google.com/uc?id={file_id}", output_file)
