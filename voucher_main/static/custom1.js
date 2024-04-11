console.log('Connected successfully')
function generatePDF(){
    const element = document.getElementById('pv');
    html2pdf()
    .from(element)
    .save('new-voucher')
    

    
    var today = new Date();
    var minutes = today.getMinutes();
    minutes = minutes > 9 ? minutes : '0' + minutes;;
    var date = 'Printed on '+today.getDate()+'-'+(today.getMonth()+1)+'-' +today.getFullYear()+' Time: '+today.getHours()+":" + minutes + " " +'Hrs';
    document.getElementById('print').textContent=date
}








   
    
    


   

