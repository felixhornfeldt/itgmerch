# Felix Lagring Code

### Sample

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

### Simple Head Code
       
            <!--Fonts-->
            <link href="https://fonts.googleapis.com/css?family=Bowlby+One+SC|Droid+Sans:400,700|Noto+Sans:400,400i,700,700i|Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i|Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Space+Mono:400,400i,700,700i" rel="stylesheet" >
            
            <!--CSS Stylesheets-->
            <link rel="stylesheet" type="text/css" href="CSS\main.css" />
            
            <!--scale and charset-->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0" >
            
            <!--Title of page-->
            <title>ITG Market</title>
            
            <!--Icon Head-->
            <link rel="icon" href="http://it-gymnasiet.se/wp-content/uploads/2017/05/cropped-itg-favicon-512x512-32x32.png" sizes="32x32" />
            <link rel="icon" href="http://it-gymnasiet.se/wp-content/uploads/2017/05/cropped-itg-favicon-512x512-192x192.png" sizes="192x192" />
            <link rel="apple-touch-icon-precomposed" href="http://it-gymnasiet.se/wp-content/uploads/2017/05/cropped-itg-favicon-512x512-180x180.png" />
            
            <!-- Icon library FB TW IG etc. -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
            
            <!-- JS Code -->
            <script src="wojodesign-simplecart-js-51a9a38/test/inc/jquery.1.6.1.min.js"></script>
            <script src="wojodesign-simplecart-js-51a9a38/simpleCart.js"></script>
            <script src="JS/main.js"></script>

### Simple header code

            <header>
                <div id="header">
                    <div id="top-header-div">
                        <div id="headline-img-txt">
                            <div id="headline" class="headline">
                                <div class="headline-img">
                                    <a class="img-bar-top-href" href="index.html">
                                        <img src="http://it-gymnasiet.se/wp-content/themes/itgymnasiet2017/img/itg_weloveit.png" alt srcset="http://it-gymnasiet.se/wp-content/themes/itgymnasiet2017/img/itg_weloveit@2x.png 200w" width="131px" height="131px" class="img-head-top-bar" />
                                    </a>    
                                </div>
                                <div class="headline-text">
                                    <h1><a class="blue">I</a><a class="pink">T</a><a class="orange">G</a> <a class="white">M</a>arketplace</h1>
                                </div>
                                <div class="cart-button">
                                    <!--<a href="shopping-cart.html">--><a onclick="showDiv()">
                                        <i class="fa fa-cart-plus"></i>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
            <div class="shopping_cart_mini hide" id="show">
                <a onclick="removeDiv()" class="remove_div_mini">X</a>
                <h1>Kundvagn</h1>
                <div class="simpleCart_items"></div>
                <p class="grand_total_p">Grand Total: <span id="simpleCart_grandTotal" class="simpleCart_grandTotal"></span></p>
                <button class="shopping_cart_mini_button"><a href="shopping-cart.html">Till Kundvagn</a></button>
            </div>
             

### Bildlänk

http://it-gymnasiet.se/wp-content/themes/itgymnasiet2017/img/itg_weloveit.png