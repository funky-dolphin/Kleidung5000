import React, { useEffect, useState } from "react";
import Transaction from "./Transaction";
import "../styles.css";

const TransactionList = ({user}) => {
    const[transactions,setTransactions]=useState([])
    useEffect(()=>{
        if(user && user.id) {
        fetch(`http://127.0.0.1:5555/favoriteitemsbyowner/${user.id}`)
        .then(res=>res.json())
        .then(data=>setTransactions(data));
        }
      },[user])
      console.log(setTransactions)

  return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 style={{ marginBottom: "20px", color: "whitesmoke" }}>
        Your Transactions
      </h3>
        {<ul className="d-flex flex-wrap justify-content-center">
          {transactions.map((transaction) => {
            return <Transaction
              transaction = {transaction}
              key={transaction.id}
              price={transaction.price}
            />;
          })}
        </ul>}
        
      </div>
  );
};

export default TransactionList;