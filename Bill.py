
#inputs
item1 = str(input("Enter the item1 name : ")) ;
price1 = float(input("Enter the unit price of item1 : Rs." ));
Quantity1 = float(input("Enter the quantity of item1 : " ));
print('-'*50)
item2 = str(input("Enter the item2 name : ")) ;
price2 = float(input("Enter the unit price of item2 : Rs." ));
Quantity2 = float(input("Enter the quantity of item2 : " ));
print('-'*50)
item3 = str(input("Enter the item3 name : ")) ;
price3 = float(input("Enter the unit price of item3 : Rs." ));
Quantity3 = float(input("Enter the quantity of item3 : " ));
print('-'*50)
item4 = str(input("Enter the item4 name : ")) ;
price4 = float(input("Enter the unit price of item4 : Rs." ));
Quantity4 = float(input("Enter the quantity of item4 : " ));
print('-'*50)
item5 = str(input("Enter the item5 name : ")) ;
price5 = float(input("Enter the unit price of item5 : Rs." ));
Quantity5 = float(input("Enter the quantity of item5 : " ));
print('-'*50)

#Discount
Discountpercentage=float(input("Enter the discount percentage :  %"));
print('-'*50)

#Company name and information
company_name = 'Greens'
company_address = '226,Highlevel Rd.'
company_city = 'Maharagama.'

print(' '*10,'='*60)
print(' '*10,' '*27,company_name,' '*25);
print(' '*10,' '*21,company_address,' '*26);
print(' '*10,' '*25,company_city,' '*26);
print(' '*10,'.'*60);
print(' '*10,"Tele:077 3861 512/0112 303 500",' '*12,"Store Code: SCMG");
print(' '*10,"26-09-2022",' '*40,"17:50:58");
print(' '*10,'-'*60)

#Formatting the prices for two decimal places
#,"{:.2f}".format()

#Bills setup
print(' '*10,"No:",' '*3,"Item",' '*5,"Quantity",' '*3,"Unit Price",' '*4,"Amount(Rs.)")
print(' '*10,'-'*60)
Total1=price1*Quantity1
print(' '*10,1,' '*4,item1,' '*8,Quantity1,' '*7,"{:.2f}".format(price1),' '*11,"{:.2f}".format(Total1));
Total2=price2*Quantity2
print(' '*10,2,' '*4,item2,' '*6,Quantity2,' '*7,"{:.2f}".format(price2),' '*11,"{:.2f}".format(Total2));
Total3=price3*Quantity3
print(' '*10,3,' '*4,item3,' '*6,Quantity3,' '*5,"{:.2f}".format(price3),' '*12,"{:.2f}".format(Total3));
Total4=price4*Quantity4
print(' '*10,4,' '*4,item4,' '*5,Quantity4,' '*5,"{:.2f}".format(price4),' '*12,"{:.2f}".format(Total4));
Total5=price5*Quantity5
print(' '*10,5,' '*4,item5,' '*1,Quantity5,' '*5,"{:.2f}".format(price5),' '*12,"{:.2f}".format(Total5));
print(' '*10,'-'*60)


#Final Calculations
Total=Total1+Total2+Total3+Total4+Total5
print(' '*10,"Gross Amount",' '*38,"{:.2f}".format(Total));
print(' '*10,"Promotion Discount (%)",' '*32,Discountpercentage);

Discount=Total*Discountpercentage/100
print(' '*10,"Discount",' '*44,"{:.2f}".format(Discount));
Netamount=Total-Discount
print(' '*10,"Net Amount",' '*40,"{:.2f}".format(Netamount))
print(' '*10,'-'*60)

#declare ending message
message = 'Thanks for shopping with us today!'
print(' '*10,' '*13,message,' '*8);
print(' '*10,' '*13,"IMPORTANT NOTICE : In case of price",' '*8);
print(' '*10,' '*13,"discrepancy, return the item & bill",' '*8);
print(' '*10,' '*11,"within 7 days for refund of difference.",' '*8);
print(' '*10,' '*25,"*",company_name,"*",' '*25);
print(' '*10,'='*60)



