# Jewellery REST shop
Training repository. It is a jewelry shop developed using the Django REST framework
___
# API
|Method | Endpoint| Description| Required |
|-------|---------|------------|----------|
|**GET**|http://localhost/customer/| Returns a list of a customers | None|
|**GET**|http://localhost/customer/{customer_id: int}| Returns a customer by id | None|
|**POST**|http://localhost/customer/| Creates customer| Body:<br> - name: string,<br> - surname: string,<br> - adress: string,<br> - phone_number:string.|
|**PUT**|http://localhost/customer/{customer_id: int}| Allows to change an entry | Body:<br> - name: string,<br> - surname: string,<br> - adress: string,<br> - phone_number:string.|
|**DELETE**|http://localhost/customer/{customer_id: int}| Allows to delete an entry | None|