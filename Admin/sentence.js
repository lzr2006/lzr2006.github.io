$(function()
{
  //句子被喜欢的次数 初始化
  var likes=0
  alert("获取今天的句子！")
  $.get("http://everydayonesentence.biu8.top/Truephp/get_today_sentence.php",function(data,status)
  {
    //document.write(data)
    console.log(data)
    $(".sentence").text(data)
  })
