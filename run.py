import os

os.system("unzip -o /model/code/TGA-without-align-dla.zip -d /model/code")

with open("/model/run.sh", "w") as f:
    
    videos = os.listdir("/dataset")

    for video in videos:
        f.write(f"mkdir /results/{video}\n")
        f.write(f"python3 /model/code/test.py --test_dir /dataset/{video} --image_out /results/{video}\n")

os.system("chmod +x /model/run.sh")
os.system("/model/run.sh")

