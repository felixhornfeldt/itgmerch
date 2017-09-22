### Sample code

    <div id="main_div">
                    <div id="shopping_cart">
                        <div id="shelf">
                            <div class="simpleCart_shelfItem">
                                <h3 class="item_t_shirt">ITG T-Shirt</h3>
                                <img src="https://i.pinimg.com/736x/b9/e9/81/b9e98191496f7bc31aa26226d30a589d--wolf-eyes-wolves-art.jpg" alt="Please reload site" class="item_pic_t_shirt" /><br>
                                <select class="item_size">
                                    <option value="X-Small">XS</option>
                                    <option value="Small">S</option>
                                    <option value="Medium">M</option>
                                    <option value="Large">L</option>
                                    <option value="X-Large">XL</option>
                                </select><br>
                                <input type="number" value="1" max="5" class="item_quantity"><br>
                                <span class="item_price">80.00kr</span><br>
                                <input type="button" class="item_add" value="Add to cart"/>
                            </div>
                        </div>
                        <div id="shopping_body_content">
                            <div class="simpleCart_items"></div>
                        </div>
                    </div>
                </div>


            <link rel="stylesheet" type="text/css" href="shop.css" >
            <link rel="stylesheet" type="text/css" href="../CSS/main.css" >
            
### För att Simplecart JS ska fungera så behövs även jquery filen, annars blir det "inte bra"
            <script src="inc/jquery.1.6.1.min.js"></script>
	        <script src="../simpleCart.js"></script>