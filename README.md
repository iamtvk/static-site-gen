# A static site generator from Markdown

 converts md files to HTML pages, similar to Hugo.


 ## Usage:
 
 1. Write your markdown files in the `content/` directory; multiple pages can be generated by writing md files in different dirs inside the `content/`.
    
 3. Store any local images in `static/images/` directory.
    
 5. You can customize the `template.html` and `static/index.css` files as per your requirements
    
 7. Run `./main.sh` ,
    - which would write html pages to `public` dir
    - Starts Python webserver at `localhost:8888`
 
 8. If all goes well, you will see a message similar to this :

    
    ![image](https://github.com/user-attachments/assets/7d514030-784e-4bec-b7fd-80fe880958e6)



 ### Note:
  - This project doesn't yet support nested in-line markdown like `**this is *some* thing **` , you will be forced to write it as ` **this is ** *some* **thing **`.
