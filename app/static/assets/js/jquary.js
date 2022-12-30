
$(document).ready(function () {
 
  if (localStorage.getItem('cart') == null) {
    var cart = {};
  } else {
   
    cart = JSON.parse(localStorage.getItem('cart'));
     
    
  }
  
  //$('.cart').click(function(){ 
    $('.divpr').on('click', 'button.cart' ,function () {
    var idstr = this.id.toString();
     
    
    if (cart[idstr] != undefined) {
      console.log("exist");
      cart[idstr][0] = cart[idstr][0] + 1;
      cart[idstr][4]=cart[idstr][4]+cart[idstr][3]
      localStorage.setItem('cart', JSON.stringify(cart));
      
    } else {
      qty = 1;
     
     
     price = document.getElementById('price' + idstr).innerHTML;
      totalPrice=document.getElementById('price' + idstr).innerHTML;
      image = document.getElementById('img' + idstr).src;
      aname = document.getElementById('name' + idstr).innerHTML;
      console.log("not");
      cart[idstr] = [qty, aname, image, parseInt(price),parseInt(totalPrice)];
    }
   
    
    localStorage.setItem('cart', JSON.stringify(cart));
    
    console.log(cart)
  });
  
    for (item in cart ) {
      let name = cart[item][1];
      let qty = cart[item][0];
      let image = cart[item][2];
      let price = cart[item][3];
      let totalPrice=cart[item][4]
      let id=item;
    // console.log(id);
      mystr =` <tr><td class="product-thumbnail"><image src="${image}" alt="product"></td>
       <td  class="product-name">${name}</td>
      <td class="product-price">$<span class="amount">${price}</span></td>
      <td  class="product-quantity">
    <button id="plus${id}"  class ="btn btn-primary plus">+</button>
    <span id="qv${id}" >${qty}</span>
    <button id="minus${id}" class="btn btn-primary minus">-</button></td>
    <td  class="product-subtotal" id="total${id}"><span>$</span>${totalPrice}</td>
    <td action="#" class="product-remove"><i class="fa fa-times"></i></td> </tr>`;
      
    
      $('#items').append(mystr)
     }
  
  
  
  
  
    $('#items').on('click','button.plus',function(){
      a=this.id.slice(6,);
    cart['pr'+a][0]=cart['pr'+a][0]+1;
    cart['pr'+a][4]=cart['pr'+a][0]*cart['pr'+a][3]
    
    //var qty=cart['pr'+a][0]
    var totalPrice1=0;
    //totalPrice=totalPrice+qty * itemPrice
    //var Inum=b;
    //var intc=parseInt(c);
    
    totalPrice1=totalPrice1+cart['pr'+a][0]*cart['pr'+a][3];
    
    document.getElementById('qvpr'+a).innerHTML=cart['pr'+a][0];
    
    document.getElementById('totalpr'+a).innerHTML=totalPrice1;
    //cart = JSON.parse(localStorage.getItem('cart'));
    
    //localStorage.setItem('totalPrice', JSON.stringify(totalPrice));
    localStorage.setItem('cart', JSON.stringify(cart));
    })
    
    $('#items').on('click','button.minus',function(){
      a=this.id.slice(7,);
    cart['pr'+a][0]=cart['pr'+a][0]-1;
    cart['pr'+a][4]=cart['pr'+a][0]*cart['pr'+a][3]
    //var qty=cart['pr'+a][0]
    var totalPrice1=0;
    
    totalPrice1=cart['pr'+a][0]*cart['pr'+a][3]-totalPrice1
    //totalPrice=qty * itemPrice-totalPrice
    document.getElementById('qvpr'+a).innerHTML=cart['pr'+a][0];
    
    document.getElementById('totalpr'+a).innerHTML=totalPrice1;
   
    //localStorage.setItem('totalPrice', totalPrice);
    localStorage.setItem('cart', JSON.stringify(cart));
  
  
 

}); 





   

      
    
  

  



 

  

});

// https://stackoverflow.com/questions/43258967/how-to-display-new-line-input-text-in-new-line
