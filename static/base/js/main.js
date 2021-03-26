function insertTextInInputValue(buttonValueIs){
    if (buttonValueIs == "AC")
    {
      $('#ques').text('Ans : 0');
      $('#result').val('');
    }
    else {
      var inputElementIs = document.getElementById("result");
      inputElementIs.value =  inputElementIs.value + buttonValueIs;
      $('#result').val(inputElementIs.value);
    }
    
}
function borrarDel(buttonValueIs){
  if(buttonValueIs == "←")
  {
    var retroceder = document.getElementById("result");

    retroceder.value = retroceder.value.substring(0, retroceder.value.length - 1);

    $('#result').val(retroceder.value);
  }
}
