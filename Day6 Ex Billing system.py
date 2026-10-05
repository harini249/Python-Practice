# billing syatem

product_prices = eval(input("Enter your product prices : "))
total_cost = sum(product_prices)
if total_cost>=10000:
    dis = (30/100)*total_cost     
    sub_total = total_cost-dis
    gst = (18/100)*sub_total     
    bill = sub_total + gst
    print(f"Bill : {bill:.2f}")
elif total_cost<=10000 and total_cost>=7000:
    dis = (20/100)*total_cost
    sub_total = total_cost - dis
    gst = (13/100)*sub_total
    bill = sub_total+gst
    print(f"Bill : {bill:.2f}")
elif total_cost <=7000 and total_cost >= 5000:
    dis = (15/100)*total_cost
    sub_total = total_cost-dis
    gst = (10/100)*sub_total
    bill = sub_total+gst
    print(f"Bill : {bill:.2f}")
