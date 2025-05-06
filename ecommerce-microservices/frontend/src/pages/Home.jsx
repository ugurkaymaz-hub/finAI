import React from "react";
import { Link } from "react-router-dom";
import "../style/Home.css"; // CSS dosyasını import ettik

function Home() {
    return (
        <div className="home">
            <h1>Hoşgeldiniz, Ana Sayfa</h1>
            <p>Burada ürünler ve diğer içerikler yer alacak.</p>
        </div>
    );
}

export default Home;
