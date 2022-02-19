# FoodCode - Developed at STHacks

A web application designed to scan barcodes and detect harmful ingredients. The application uses OpenCV to allow the user to use their device's webcam to scan a barcode. The barcode is then processed and a request is sent to Barcode Lookup API, which returns a list of ingredients for the given barcode. The ingredients are then filtered through our database of harmful ingredients and any matches are displayed to the user. 

Built using:
- Django framework
- Barcode Lookup API
- OpenCV

## Challenges

This was the first time many of our team members had worked on Django so initial progress was slow. However, everyone was soon able to catch up with the ins and outs of Django, which brought us to our next challenge - retrieving the ingredients of a product through its barcode. For that, we used the free tier in Barcode Lookup API, a service that takes a barcode as an input and returns a list of ingredients. As we had zero experience with JavaScript, implementing an API connection and developing a seamless user experience through AJAX requests was extremely difficult. Due to a lack of understanding, our AJAX requests kept giving us visual artefacts and didn't update the interface as we wanted them to.

## Future Goals

Our future goal is to convert this application into a functioning Android/IOS app. We figured that due to the nature of the idea, it would be best suited for a mobile app. But, we didn't have any experience with developing mobile applications, so we instead opted for a web application. 
