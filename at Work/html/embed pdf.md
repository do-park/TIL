# embed pdf

1. using `iframe`

   ```html
   <div id="pdf">
     <iframe src="pdf.html" style="width: 100%; height: 100%;" frameborder="0" scrolling="no">
       <p>It appears your web browser doesn't support iframes.</p>
     </iframe>
   </div>
   ```

   

2. using `embed`

   ```html
   <body>
       <object data="lorem.pdf" type="application/pdf">
           <p>It appears you don't have Adobe Reader or PDF support in this web browser. <a href="lorem.pdf">Click here to download the PDF</a>. Or <a href="http://get.adobe.com/reader/" target="_blank">click here to install Adobe Reader</a>.</p>
          <embed type="application/pdf" width="100%" height="100%"/>
       </object>
   </body>
   ```



c.f. pdf only

```html
#toolbar=0&amp;navpanes=0&amp;scrollbar=0&amp;statusbar=0&amp;messages=0&amp;scrollbar=0
```

- <object> data 뒤에 추가