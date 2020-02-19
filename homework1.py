# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:55:47 2020

@author: Yakre
"""
import datetime
import random

class MutualFund:
    
    funds=[]
    
    def _init_(self,mfname):
        self.mfname=mfname
        self.funds.append(self.mfname)
        
    def mflist():
        return "MF:"+str(MutualFund.funds)

class Stock:
    
    stocks={}
    
    def _init_(self,sprice,sname):
        self.sprice=sprice
        self.sname=sname
        self.stocks.update({self.sname : self.sprice})
        
    def slist():
        return "S:"+str(Stock.stocks)


class Portfolio:
    
    portmflist={}
    portslist={}
    
    def __init__(self, balance=0):
        self.balance = balance
        self.mflist=MutualFund.mflist()
        self.slist=stock.slist()
        self.transactions = []
    
    def addCash(self, amount):
        self.balance += amount
        self.transactions.append(+amount)
        return amount
    
    def withdrawCash(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            self.transactions.append(-amount)
            return amount
        else:
            return 'Insufficient Funds' 
    
    def buyMutualFund(self,mfqtt,value):
        self.MutualFundQuantity=mfqtt
        
        if self.balance>=1*mfqtt:
            self.transactions.append(str(datetime.date.today())+" : "+str(mfqtt)+" "+value.mfname+"mutual fund acquired")
            self.balance=self.balance-1*mfqtt
        else:
            return 'Insufficient Funds'
   
    def sellMutualFund(self,mfqtt,mfname):
        self.MutualFundQuantity=mfqtt
        
        if self.portmflist[mfname]>=self.MutualFundQuantity:
            profit=round(random.uniform(0.9,1.2)*self.MutualFundQuantity,2)
            self.transactions.append(str(datetime.date.today())+" : "+str(mfqtt)+" "+value.mfname+"mutual fund sold")
            self.balance+=profit
            self.portmflist[mfname]-=self.MutualFundQuantity
    
    def buyStock(self,sqtt,value):
        self.StockQuantity=sqtt
        
        if self.balance>=value.sprice*sqtt:
           self.transactions.append(str(datetime.date.today())+" : "+str(sqtt)+" "+value.sname+"stock acquired")
    """------------"""
        else:
            return 'Insufficient Funds' 
        
    def sellStock(self,sname,sqtt):
        self.StockQuantity=sqtt
        
        if self.portslist[sname]>=self.StockQuantity:
        profit=round(Stock[sname] random.uniform(0.5,1.5)*sqtt,2)
        self.transactions.append(str(datetime.date.today())+" : "+str(sqtt)+" "+sname+"stock was sold")
        self.balance+=profit
        self.portslist[sname]-=self.StockQuantity
    
    
    def get_balance(self):
        return self.balance
    
    def recent_transactions(self):
        if len(self.transactions) < 1:
            return None
        else:
            return self.transactions.pop()