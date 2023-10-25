import React, { Component } from 'react';
import Product from "./Product";

export default class App extends Component {

  render() {
    return (
      <div className='app'>
        <div className='products-item-wrapper'>
          <Product />
          <Product />
          <Product />
          <Product />
          <Product />
          <Product />
        </div>
      </div>
    );
  }
}
