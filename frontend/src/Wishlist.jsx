import React, { useState, useEffect } from 'react'

function Wishlist(props){
    useEffect(() => {
        if (props.wishList.length === 0){
            document.getElementById('wishlist_none').style.display = 'block'
            document.getElementById('wishlist_results').style.display = 'none'
        }
        else{
            document.getElementById('wishlist_none').style.display = 'none'
            document.getElementById('wishlist_results').style.display = 'block'
        }
    }, [props.wishList])

    return(
        <div id='wishlist_container'>
            <form action="/homepage" method='POST'>
                <button class="btn btn-primary" type="submit">Go to homepage</button>
            </form>
            <h1 id='wishlist_none'>Your wishlist is empty</h1>
            <div id='wishlist_results'>
            {props.wishList.map((item, index) => (
                <div key={index}>
                    <form action="/deletewish" method="POST">
                        <div className="card text-center">
                            <div className="card-header">{index+1}</div>
                            <div className="card-body">
                                <h5 className="card-title">{item[1]}</h5>
                                <input type="hidden" name="product_name" value={item[1]} />
                                <p className="card-text">${item[2]}</p>
                                <p className="card-text">{item[3]} ⭐</p>
                            </div>
                            <div className="card-footer text-body-secondary">
                                <button type="submit" className="btn btn-primary">
                                    Remove from wishlist
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            ))}
            </div>
        </div>
    )
}

export default Wishlist