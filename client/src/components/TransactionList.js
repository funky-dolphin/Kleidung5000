import React, { useEffect, useState } from "react";
import Transaction from "./Transaction";
import "../styles.css";
import styles from "./Marketplace.module.css";

const TransactionList = ({user}) => {
    const[transactions,setTransactions]=useState([])
    useEffect(()=>{
        if(user && user.id) {
        fetch(`/transactions/${user.id}`)
        .then(res=>res.json())
        .then(data=>setTransactions(data));
        }
      },[user])

      console.log(setTransactions)

  return (
    <div className="d-flex flex-column align-items-center pt-5 text-center">
      <h3 className={styles.glitch} data-text="Your Purchases">
        Your Purchases
      </h3>
        {<ul className="d-flex flex-wrap justify-content-center">
          {transactions.map((transaction) => {
            return <Transaction
              transaction = {transaction.id}
              key={transaction.id}
              seller_id={transaction.users.name}
              price={transaction.price}
              name={transaction.item_name}
              image={transaction.image}

            />;
          })}
        </ul>}
        
      </div>
  );
};

export default TransactionList;