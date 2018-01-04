# FileIO
Personal Used. Some File Operation in daily deep learning work.


### utf_io
Codes abou reading and writing text file for CAFFE.   
A typical file is like.  
**/path/to/the/image.jpg  somelabel**
i.e.  A typical text file to train a classification network
```
/home/hyichao/temp/lena1.jpg 1
/home/hyichao/temp/lena2.jpg 2
```
or the following, to train a CNN-RNN network for scene text recognition
```
/home/hyichao/temp/abcd.jpg StarBuck   
/home/hyichao/temp/abcd.jpg H&M
```

While using utf8_io to read in lines, using codes as follows
```
import utf8_io
lines = utf8_io.read_lines('test/test-utf8.txt')
paths, labels = utf8_io.read_sublines('test/test-utf8.txt')
```

***FYI, using \t to sepearte path and label, since label might contain a sementic space***

### image_io
TODO

### file_io
TODO

### statistic
TODO
