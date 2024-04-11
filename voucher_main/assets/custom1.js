
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
Document.getElementById('test').textContent='Test test'
function valityChecker(){
    var date1=Document.getElementById('date1');
    var date2 =Document.getElementById('date2');
    if (date2>date2) {
        Document.getElementById('btns').addClass('disabled');
        
    }

}


