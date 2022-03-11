

function onlyNumbers(evt) {
  var e = event || evt; // For trans-browser compatibility
  var charCode = e.which || e.keyCode;

  if (charCode > 31 && (charCode < 48 || charCode > 57))
      return false;
  return true;
}

function NumToWord(inputNumber) {
  var str = new String(inputNumber)
  var splt = str.split("");
  var rev = splt.reverse();
  var once = ['Zero', ' One', ' Second', ' Third', ' Fourth', ' Fifth', ' Sixth', ' Seventh', 'Eighth', ' Ninth'];
  var twos = ['Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen'];
  var tens = ['', 'Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety'];

  numLength = rev.length;
  var word = new Array();
  var j = 0;

  for (i = 0; i < numLength; i++) {
      switch (i) {

          case 0:
              if ((rev[i] == 0) || (rev[i + 1] == 1)) {
                  word[j] = '';
              }
              else {
                  word[j] = '' + once[rev[i]];
              }
              word[j] = word[j];
              break;

          case 1:
              aboveTens();
              break;

          case 2:
              if (rev[i] == 0) {
                  word[j] = '';
              }
              else if ((rev[i - 1] == 0) || (rev[i - 2] == 0)) {
                  word[j] = once[rev[i]] + " Hundred ";
              }
              else {
                  word[j] = once[rev[i]] + " Hundred and";
              }
              break;

          case 3:
              if (rev[i] == 0 || rev[i + 1] == 1) {
                  word[j] = '';
              }
              else {
                  word[j] = once[rev[i]];
              }
              if ((rev[i + 1] != 0) || (rev[i] > 0)) {
                  word[j] = word[j] + " Thousand";
              }
              break;

              
          case 4:
              aboveTens();
              break;

          case 5:
              if ((rev[i] == 0) || (rev[i + 1] == 1)) {
                  word[j] = '';
              }
              else {
                  word[j] = once[rev[i]];
              }
              if (rev[i + 1] !== '0' || rev[i] > '0') {
                  word[j] = word[j] + " Lakh";
              }
               
              break;

          case 6:
              aboveTens();
              break;

          case 7:
              if ((rev[i] == 0) || (rev[i + 1] == 1)) {
                  word[j] = '';
              }
              else {
                  word[j] = once[rev[i]];
              }
              if (rev[i + 1] !== '0' || rev[i] > '0') {
                  word[j] = word[j] + " Crore";
              }                
              break;

          case 8:
              aboveTens();
              break;

          default: break;
      }
      j++;
  }

  function aboveTens() {
    if (rev[i] == 0) { word[j] = ''; }
    else if (rev[i] == 1) { word[j] = twos[rev[i - 1]]; }
    else { word[j] = tens[rev[i]]; }
  }
  word.reverse();
  var finalOutput = '';
  for (i = 0; i < numLength; i++) {
      finalOutput = finalOutput + word[i];
  }
  return finalOutput;
}

function restAmount(){
    
  var participent_no=$("#myinput3").val();
  
  if (document.getElementById("chk1").checked){
    //   alert("checked"+document.getElementById("chk1").checked);
    if(parseInt($('#total_chq').val())<=participent_no)
    {
        let result=participent_no-parseInt($('#total_chq').val());
        

        let total_amount=parseInt($('#myInput1').val());
        
        let calc_amount=0;
        for(let i=1;i<parseInt($('#total_chq').val());i++){
            
        
            calc_amount=calc_amount+ parseInt($('#new_'+i).val());
            
            
        
        
    }
        
        alert("calc_amount"+calc_amount);
        let rem_amount=total_amount-calc_amount;
     
        let totalResult=parseInt(result)+parseInt(1);
        
        //alert("totalResult"+totalResult);
        let equal_amount=rem_amount/totalResult;
        //alert(rem_amount+"########## result: "+parseInt(result)+parseInt(1)+"##### rem_amount: "+equal_amount);
        //alert(equal_amount);
            for(let i=0;i<=result;i++){
                
                add('equaldivide',parseInt($('#total_chq').val()),equal_amount);
                
                
            }
    }
}
else{
    //alert(parseInt($('#total_chq').val())+"#######"+participent_no);
    if(parseInt($('#total_chq').val())<=participent_no)
    {
        add('position',parseInt($('#total_chq').val())+1,0);
    }
}
}

function add(from,position,amt){
   
        // $('#new_chq').val("");
        // $('#new_chq').html('');
       let equal_amount=0;
   let total_amount=parseInt($('#myInput1').val());
   let first_po_val="";
    //let total_row=$('#total_chq').val();
   
    let pos1_amount=parseInt($('#new_1').val());
    let total_row=(parseInt($('#myinput3').val()))-1;

   
    
    //alert("position" +position);
    

   
    
    let total_row_sum=0;
    
   // for(let i=2;i<=total_row+1;i++){
    let new_chq_no_in_word=NumToWord(position)
    alert(position)
        let new_input="<span id='p_"+position+"'>"+new_chq_no_in_word+" Position </span><input type='text' id='new_"+position+"' name='reamt' value='"+position+"' class='form-control'>";
        $('#new_chq').append(new_input);
        $('#new_'+position).val(amt);
        $('#total_chq').val(parseInt($('#total_chq').val())+1);
   // }




//     ============================================================
//     let participant=$('#myinput3').val();
//     let calc_amount=0;
//    let total_amount=$('#myInput1').val();
// //    let total_amount=$('#myInput1').val();
//    if(total_amount==""){
     
//    }
//    let first_po_val="";
//     let total_row=$('#total_chq').val();
   
    
//     let total_row_sum=0;
//     //for(let i=0;i<=participant;i++){
//         // alert(i)
//       total_row_sum = total_row+parseInt($('#new_'+position).val());
  
//    // }
//     // alert(total_row_sum+"="+total_amount)
//     if (total_row_sum < total_amount){

//     let new_chq_no = parseInt($('#total_chq').val())+1;
//     // alert(new_chq_no)
    
//     let new_chq_no_in_word=NumToWord(new_chq_no);
//     if (from =='equaldivide'){
//     //let first_po_val=$('#new_1').val();
//     var participent_rest=$("#myinput3").val();
//     //alert("position "+position);
   
//     for(let i=0;i<position;i++){

//         calc_amount=calc_amount+$('#new_'+position).val()
//         //alert("amount "+$('#new_'+position).val());
//     }
//     first_po_val=(total_amount-calc_amount)/(participent_rest-1);
 
//     }else{
//        first_po_val="";
//     } 

//     let new_input="<span id='p_"+new_chq_no+"'>"+new_chq_no_in_word+" Position </span><input type='text'  id='new_"+new_chq_no+"' name='reamt' value='"+Math.round(first_po_val)+"' class='form-control'>";
//     $('#new_chq').append(new_input);
//     $('#total_chq').val(new_chq_no);
 // }
}

function remove(){
  //alert('dfsdfsd');
  var last_chq_no = parseInt($('#total_chq').val());
  alert(last_chq_no)
  //$('#total_chq').val(parseInt($('#total_chq').val())-1);

  if(last_chq_no>1){
    $('#p_'+last_chq_no).remove();
    $('#new_'+last_chq_no).remove();
    $('#total_chq').val(last_chq_no-1);
    
  }
}

    

  function validateForm() {
        let k = document.forms["myForm"]["category"].value;
        let a = document.forms["myForm"]["question"].value;
        let b = document.forms["myForm"]["no_winner"].value;
        let s = document.forms["myForm"]["type_price"].value;
        let c = document.forms["myForm"]["contest_image_thumb"].value;
        // let c = document.forms["myForm"]["contest_image_thumb"].value;
        let f = document.forms["myForm"]["total_amount"].value;
        let d = document.forms["myForm"]["contestWinTitle"].value;
        let e = document.forms["myForm"]["contestWinAmountTitle"].value;
        let m = document.forms["myForm"]["sponsor_id"].value;
        let ht = document.forms["myForm"]["uploadContest"].value;
        let j = document.forms["myForm"]["contest_start_date"].value;
        let z = document.forms["myForm"]["contest_start_time"].value;
        let o = document.forms["myForm"]["contest_end_date"].value;
        let p = document.forms["myForm"]["contest_end_time"].value;

        
            
            
            if (k == "") {
            alert("Category is blank");
            return false;
            }
            if (a == "") {
            alert("Question is blank");
            return false;
            }
            if (b == "") {
            alert("No of Winner is blank");
            return false;
            }
            if (s == "") {
            alert("Prize type is blank");
            return false;
            }
            if (c == "" && document.getElementById("img11") == null) {
            alert("Prize image is blank");
            return false;
            }
            if (f == "") {
            alert("Prize Amount is blank");
            return false;
            }
            if (d == "") {
            alert("contestWinTitle is blank");
            return false;
            }
            if (e == "") {
            alert("contestWinTitleAmountTitle is blank");
            return false;
            }
            if (m == "") {
            alert("Sponcer is blank");
            return false;
            }
            if (ht == "") {
            alert("Contest Creative is blank");
            return false;
            }
           
            if (j == "") {
            alert("The Start Date Field is blank");
            return false;
            }
            if (z == "") {
            alert("The Start Time Field is blank");
            return false;
            }
            if (o == "") {
            alert("The End Date Field is blank");
            return false;
            }
            if (p == "") {
            alert("The End Time Field is blank");
            return false;
            }
            
            
            
            
 
    
        }
  
  CKEDITOR.replace( 'editor1', {
					fullPage: true,
					extraPlugins: 'docprops',
					allowedContent: true,
					height: 250
				} );
  CKEDITOR.replace( 'editor2', {
					fullPage: true,
					extraPlugins: 'docprops',
					allowedContent: true,
					height: 250
				} );
  CKEDITOR.replace( 'editor3', {
					fullPage: true,
					extraPlugins: 'docprops',
					allowedContent: true,
					height: 250
				} );


    function myChangeFunction(input1) {
        var input2 = document.getElementById('myInput2');
        input2.value = input1.value;
        }

    function yesnoCheck() {
    if 
    (document.getElementById('yesCheck').checked) {
    document.getElementById('ifYes').style.display = 'block';
    document.getElementById('myvideo','myurl').value = '';
    document.getElementById('myurl').value = '';

    
    }
    else document.getElementById('ifYes').style.display = 'none';

    
    if 
    (document.getElementById('noCheck').checked) {
    document.getElementById('ifno').style.display = 'block';
    document.getElementById('myimage').value = '';
    }
    else document.getElementById('ifno').style.display = 'none';

    

    if 
    (document.getElementById('position').checked) {
    document.getElementById('positionwise').style.display = 'block';
    }
    else document.getElementById('positionwise').style.display = 'none';

    if 
    (document.getElementById('positionone').checked) {
    var input3 = document.getElementById('myinput3');
    var input5 = document.getElementById('myInput1');
        if (input3.value==""){
            alert('Please Fill Amount and No of Winners First')
        }else if(input5.value==""){
            alert('Please Fill Amount and No of Winners First')
        }else{
    document.getElementById('positiononewise').style.display = 'block';
    }}
    else document.getElementById('positiononewise').style.display = 'none';

    
    if 
    (document.getElementById('participant').checked) {
    document.getElementById('participantwise').style.display = 'block';
    }
    else document.getElementById('participantwise').style.display = 'none';

    
    if 
    (document.getElementById('featured').checked) {
    document.getElementById('featurewise').style.display = 'block';
    }
    else document.getElementById('featurewise').style.display = 'none';

    
    if 
    (document.getElementById('mobilefeatured').checked) {
    document.getElementById('mobilefeaturewise').style.display = 'block';
    }
    else document.getElementById('mobilefeaturewise').style.display = 'none';

    
    if 
    (document.getElementById('other').checked) {
    document.getElementById('otherwise').style.display = 'block';
    }
    else document.getElementById('otherwise').style.display = 'none';

    
    if 
    (document.getElementById('gcode').checked) {
    document.getElementById('gcodewise').style.display = 'block';
    document.getElementById('myadvimage').value = '';
    document.getElementById('myadvurl').value = '';

    }
    else document.getElementById('gcodewise').style.display = 'none';

    
    if 
    (document.getElementById('cumg').checked) {
    document.getElementById('cumgwise').style.display = 'block';
    document.getElementById('myadver').value = '';
    }
    else document.getElementById('cumgwise').style.display = 'none';

    if 
    (document.getElementById('ggcode').checked) {
    document.getElementById('ggcodewise').style.display = 'block';
    document.getElementById('myadv1img').value = '';
    document.getElementById('myadv1url').value = '';

    }
    else document.getElementById('ggcodewise').style.display = 'none';

    
    if 
    (document.getElementById('ccumg').checked) {
    document.getElementById('ccumgwise').style.display = 'block';
    document.getElementById('exampleInputEmail').value = '';
    }
    else document.getElementById('ccumgwise').style.display = 'none';

    if 
    (document.getElementById('goog').checked) {
    document.getElementById('googwise').style.display = 'block';
    document.getElementById('myadv2img').value = '';
    document.getElementById('myadv2url').value = '';

    }
    else document.getElementById('googwise').style.display = 'none';

    
    if 
    (document.getElementById('cust').checked) {
    document.getElementById('custwise').style.display = 'block';
    document.getElementById('myadv2text').value = '';
    }
    else document.getElementById('custwise').style.display = 'none';
    }

    $('input.rbdonation').change(function() {
    $('#plaque_cost').val(this.value);
    });


    function myChangeFunction(input1) {
    var input3 = document.getElementById('myinput3');
    var input2 = document.getElementById('myInput2');
   
    input2.value = Math.round(input1.value/input3.value);
    
    
  }
   
  function mydateChangeFunction(input1) {
        var input2 = document.getElementById('conendate');
        input2.value = input1.value;
        }


   

