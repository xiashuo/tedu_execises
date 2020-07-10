## 选择题(每题3分，共30分)

1. 下面的变量的声明可能有错误的是：（D）多选

   A.var b=128; 

   B.b=null; 

   C.var a,b; 

   D.var a=c; 

2. 下列代码的输出结果是：（B）单选

   var a,b=10;

   console.log(a);

   console.log(b);

   

   A.10 10

   B.undefined 10

   C.10 undefined

   D.undefined undefined

3. 下列哪些选项会发生强制数据类型转换的是：（ A,B,C,D）多选

   A.Number()

   B.parseInt() 

   C.parseFloat() 

   D.String()

4. 以下程序的变量c的结果为：（D）单选

   var a,b,c;

   a = '2';

   b = 2;

   c = a+b;

​		A.22

​		B.4

​		C."4"

​		D."22"

5. 以下代码运行i的结果为：（B）单选

   var i = 8;

   do{

   ​	i++;

   }while(i>100);

   A.8

   B.9

   C.100 

   D.101

6.下列代码执行后，num的结果是：（C）单选

​	var num;

​	num=5+true

​	A.undefined

​	B.5		

​	C.6		

​	D.true

7. 下列JS标识符，错误的是：（D,E）多选

   A. _sys_varl   

   B. $change  

   C. User_name  

   D. 1_file  

   E. car.taxi

8. alert()的作用是：（D）单选

   A.弹出新窗口

   B.弹出对话框，让用户选择确认或取消

   C.弹出对话框，让用户输入内容  

   D.弹出对话框，对话框的内容是alert的参数  

9. 下列代码在输入框中输入4时输出结果是：（B）单选

   var x = prompt('请输入数字')；

   switch(x){

   ​	case "1":alert("one");

   ​	case "2":alert("two");

   ​	case "3":alert("three");

   ​	case "4":alert("four");

   ​	case "5":alert("five");

   }

   A. four

   B. four five  

   C. five  

   D. 程序出错

10.下列代码的输出结果是：（A）单选

​	var j=0;

​	for(var i=0;i<100;i++){

 	 	j=j++;

​	}

​	console.log(j);

​	A.0  

​	B.99  

​	C.100  

​	D.101

## 编程题（共40分）：

1. 求出当前时间距离第二天0点0时0分的时间差，并在页面中显示相差的时间（15分）

   ```html
    <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Document</title>
   </head>
   <body>
     <h1 id="time" style="color: red;"></h1>
       <script>
   ​    function get_time() {
   ​      var timestamp = new Date().getTime();
   ​      var tomorrow= new Date(newDate().toLocaleDateString()).getTime()+60*60*24*1000
   ​      var hour = Math.floor((tomorrow - timestamp) / (60 * 60 * 1000));
   ​      var minute = Math.floor((tomorrow - timestamp) % (60 * 60 * 1000) / (1000 * 60))
   ​      var second = Math.floor((tomorrow - timestamp) / 1000 - hour * 3600 - minute * 60)
   ​      var show_time = document.getElementById('time')
   ​      show_time.innerHTML = "距离下一天还有：" + hour + "小时 " + minute + "分钟 " + second + "秒"
   ​    }
   ​    setInterval(get_time,1);
     </script>
   </body>
   </html>
   ```

   

2. 编写程序求1到10的和并输出该结果?（10分）

   ```html
   <!DOCTYPE html>
   
   <html lang="en">
   
   <head>
   
       <meta charset="UTF-8">
   
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
     <title>Document</title>
   
   </head>
   
   <body>
   
       <script>
   
   ​    var sum = 0;
   
   ​    for (var i = 1; i <= 10; i++) {
   
   ​      sum += i
   
   ​    }
   
   ​    alert("1到10的和为："+sum)
   
     </script>
   
   </body>
   
   </html>
   ```

   

3. 编写程序找出以下数组中最大元素的下标位置及该元素的值?（15分）

   var arr={10,9,1,20,19,30,5};

   ```html
   <!DOCTYPE html>
   
   <html lang="en">
   
   <head>
   
       <meta charset="UTF-8">
   
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
     <title>Document</title>
   
   </head>
   
   <body>
   
       <script>
   
   ​    var arr = [10, 9, 1, 20, 19, 30, 5];
   
   ​    var max_value = arr[0];
   
   ​    var max_index = 0;
   
   ​    for (var i = 1; i < arr.length; i++) {
   
   ​      if (arr[i] > max_value){
   
   ​        max_value = arr[i];
   
   ​        max_index = i;
   
   ​      }
   
   ​        
   
   ​    }
   
   ​    alert("最大元素下标为："+max_index+",最大值为："+max_value)
   
     </script>
   </body>
   </html>
   ```

   

## 简答题（每题15分，共30分）:

### 1. documen.write和 innerHTML 的区别？

答：documen.write 是直接在整个文档中写入代码。会覆盖掉其他已有代码。

innerHTML 是选中一个节点后，修改节点里面的代码，只影响当前节点。

### 2. null和undefined的区别？

答：null转为数值时为0；undefined转为数值时为NaN。

当声明的变量还未被初始化时，变量的默认值为undefined。 null用来表示尚未存在的对象

undefined表示"缺少值"，就是此处应该有一个值，但是还没有定义。通常由程序返回：

（1）变量被声明了，但没有赋值时，就等于undefined。

（2）调用函数时，应该提供的参数没有提供，该参数等于undefined。

（3）对象没有赋值的属性，该属性的值为undefined。

（4）函数没有返回值时，默认返回undefined。

 

 

 