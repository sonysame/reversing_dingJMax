### reversing_dingJMax

![](https://user-images.githubusercontent.com/24853452/52542730-34054780-2de6-11e9-99e9-76674fea4776.png)

This is like Rhythm-Star game. The flag shown changes when we type 'd', 'f', 'j', 'k'. We have to know the correct order of these four characters. Also, the timing is also not constant. We can assume that if we type these four characters in correct order and timing, we can get the real flag.

![](https://user-images.githubusercontent.com/24853452/52542816-04a30a80-2de7-11e9-90ec-d7f1eab5aa55.png)

'o' is stored in either byte\_60764c, byte\_60764d, byte\_60764e, or byte\_60764f. 

Firstly, what I did was to change *usleep(0x3E8u);*. I made it really slow, and noticed that the correct order starts with "jfdfddd...".

![](https://user-images.githubusercontent.com/24853452/52542905-03261200-2de8-11e9-823c-0eb45435e6fb.png)

"jfdfddd..." order can be found on the data area. So, now we know the correct order and timing of "jfdk". 

However, when I gave the correct "jfdK", I couldn't get the flag. 

![](https://user-images.githubusercontent.com/24853452/52542966-952e1a80-2de8-11e9-8ede-f42607fb8c37.png)

The reason is it takes 19 units of time for byte\_60764c, byte\_60764d, byte\_60764e, or byte\_60764f to be checked. 

(The unit of time is 20, because the v16 satisfies the condition only when the v16 is multiple of 20.) 
![](https://user-images.githubusercontent.com/24853452/52542993-db837980-2de8-11e9-9d8f-34d85209fa46.png)