# Well Formed Formulae
### Connectives
1. ```Negation``` : ```!``` <br/>
2. ```And``` : ```^``` <br/>
3. ```Or``` : ```|``` <br/>
4. ```Implication``` : ```>``` <br/>
5. ```Equivalence``` : ```-```  <br/>
### Atoms
 ```Atoms available``` : ```[a-z] & [A-Z]``` <br/>
### Input examples
###### Node: an additional pair of ( ) is required to enclose the original formula
 ```(A|B)``` <br/>
 ```((A>B)|(!C))``` <br/>
 ```((A-B)^(C|(!A)))>A)```
#### Programs available
* ```checkWFF``` - checks if the given formula is a well formed formula 
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/K0cbrfM.png)

      </details>
     
* ```interpTruth``` - computes truth value of WFF under a specific interpretation
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/4QWfU8z.png)

      </details>
      
* ```interpsAndValidity``` - computes truth value of WFF under all interpretations & validity of WFF    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/uxbQIJp.png)

      </details>
      
* ```interpsAndValidity2``` - same as ```interpsAndValidity``` but table view
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/iOYtIF4.png)

      </details>
      
* ```subfInterpsAndValidity``` - computes interpretation for all truth values of all subformulas of a WFF
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/8CfI9gb.png)

      </details>
            
###### Node: programs above depend on ```lcsHelperFunc.py```

# WFF Relaxation
### Connectives
1. ```Negation``` : ```!``` <br/>
2. ```And``` : ```^``` <br/>
3. ```Or``` : ```|``` <br/>
4. ```Implication``` : ```>``` <br/>
5. ```Equivalence``` : ```-```  <br/>
### Atoms
 ```Atoms available``` : ```[a-z] & [A-Z]``` <br/>
### Input examples
 ```A|B```  <br/>
 ```A>B|(!C)``` <br/>
 ```(A-B)^(C|!A))>A``` <br/>
 ```A>B|C^D```
#### Programs available
* ```relaxedToStrong``` - convert a formula from relaxed form to strong from
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/6k3h4R4.png)

      </details>
      
* ```convertToNNF``` - convert formula to Negation Normal Form (NNF)
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/DAAVw45.png)

      </details>
      
* ```convertToCNF``` - convert formula to Conjunctive Normal Form (CNF)
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/AeP4p5g.png)

      </details>
      
###### Node: programs above depend on ```relHelperFunc.py```

# Clauses
### Connectives
```Negation``` : ```!``` <br/>
### Atoms
 ```Atoms available``` : ```[a-z] & [A-Z]``` <br/>
### Input examples (clause set)
```A,B``` <br/>
```!A,B``` <br/>
```!B``` <br/>
```A,B``` <br/>

### Programs available
* ```satOrUnsat``` - check if a clause set if Satifsiable or Unsatisfiable
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/o3q3zQH.png)

      </details>
      

