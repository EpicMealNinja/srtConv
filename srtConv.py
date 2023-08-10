import os


def main():
   #Create a folder for the textgrid files
   if not os.path.exists("srt"):
      os.makedirs("srt")

   #Open folder with all textgrid files
   os.chdir("textgrid")

   #Convert all textgrid files to srt files
   for file in os.listdir(r'./'):
      if file.endswith(".TextGrid"):
         textgridToSrt(file)
         os.chdir("../textgrid")

   return

def textgridToSrt(file):
   textG = open(file, "r", encoding="utf-8")
   subs = textG.read()
   subs = subs.split('\n')
   for i in range(len(subs)):
      if subs[i] == subs[len(subs)-1]:
         subs = subs[:i+1]
         break
   subs = subs[12:]

   os.chdir("../srt")
   srt = open(file[:len(file)-9] + "-subs.srt", "w", encoding="utf-8")

   for i in range(int(len(subs) / 3)):
      srt.write(str(i+1) + "\n")

      start = float(subs[i*3])
      end = float(subs[i*3+1])
      msg = subs[i*3+2]

      startHours = int(start/60/60)
      start -= startHours*60*60
      startMins = int(start/60)
      start -= startMins*60
      startStr = str(startHours) + ":" + str(startMins) + ":" + str(int(start)) + "," + str(int(1000*(start-int(start))))

      endHours = int(end/60/60)
      end -= endHours*60*60
      endMins = int(end/60)
      end -= endMins*60
      endStr = str(endHours) + ":" + str(endMins) + ":" + str(int(end)) + "," + str(int(1000*(end-int(end))))

      srt.write(startStr + " --> " + endStr + "\n")

      srt.write(msg + "\n\n")
   #Delete the last two line in srt file on all platforms
   srt.seek(0, os.SEEK_END)
   srt.seek(srt.tell() - 2, os.SEEK_SET)
   srt.truncate()

   

   srt.close()
   textG.close()
   return




if __name__ == "__main__":
   main()