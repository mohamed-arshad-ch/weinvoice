from .models  import *
from django.shortcuts import get_object_or_404


class CreateInvoiceController:
    
    def __init__(self, *args, **kwargs):
        
        self.data = kwargs['data']
    
    def create(self):
        address = self.data['address']
        cgst = self.data['cgst']
        city = self.data['city']
        comapny_address = self.data['company_address']
        company_city = self.data['company_city']
        company_district = self.data['company_district']
        company_email = self.data['company_email']
        company_gstin = self.data['company_gstin']
        company_location = self.data['company_location']
        company_logo = self.data['company_logo']
        company_name = self.data['company_name']
        company_phone = self.data['company_phone']
        company_pin = self.data['company_pin']
        company_state = self.data['company_state']
        company_signature = self.data['company_signature']
        district = self.data['district']
        email = self.data['email']
        gst_number = self.data['gst_number']
        gst_type = self.data['gst_type']
        location = self.data['location']
        logo = self.data['logo']
        name = self.data['name']
        phone = self.data['phone']
        pincode = self.data['pincode']
        product_list = self.data['product_list']
        sgst = self.data['sgst']
        due_amount = self.data['due_amount']
        state = self.data['state']
        typeof = self.data['invoice_type']

        cust, created = Customer.objects.get_or_create(name=name,logo=logo,address=address,city=city,location=location,pincode=pincode,state=state,district=district,gst_number=gst_number,gst_type=gst_type,email=email,phone=phone)
        invoice = Invoice()
        invoice.customer = cust
        invoice.company_name = company_name
        invoice.comapny_address = comapny_address
        invoice.company_city = company_city
        invoice.company_location = company_location
        invoice.company_pin = company_pin
        invoice.company_district = company_district
        invoice.company_state = company_state
        invoice.company_gstin = company_gstin
        invoice.company_email = company_email
        invoice.company_phone = company_phone
        invoice.company_logo = company_logo
        invoice.due_amount = due_amount
        invoice.sgst = sgst
        invoice.cgst = cgst
        invoice.status = True
        invoice.invoice_type = typeof
        invoice.company_signature = company_signature
        invoice.save()
    # print(product_list)
        for i in product_list:
            
            inventory = get_object_or_404(Inventory,id=i['id'])
            orderitem = OrderItems.objects.create(product=inventory,qty=i['qty'])
            oj = get_object_or_404(OrderItems,id=orderitem.id)

            invoice.product_list.add(OrderItems.objects.get(id=orderitem.id))
            stock_manage=self.stock_control(inventory,orderitem.qty)
        return invoice
        

    def stock_control(self,instance,quatity):
        print(instance.stock)
        print(quatity)
        instance.stock-=quatity
        instance.save()

