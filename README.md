# Well Formed Formulae
### Connectives
1. ```Negation``` : ```!``` <br/>
2. ```And``` : ```^``` <br/>
3. ```Or``` : ```|``` <br/>
4. ```Implication``` : ```>``` <br/>
5. ```Equivalence``` : ```-```  <br/>
6. ```Atoms possible``` : ```[a-z] & [A-Z]``` <br/>
### Input examples
###### Node: an additional pair of ( ) is required to enclose the original formula
 ```(A|B)``` <br/>
 ```((A>B)|(!C))``` <br/>
 ```((A-B)^(C|(!A)))>A)```
#### Programs available
* ```checkWFF``` - checks if the given formula is a well formed formula 
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/o3q3zQH.png)

      </details>
     
* ```interpTruth``` - computes truth value of WFF under a specific interpretation
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/o3q3zQH.png)

      </details>
      
* ```interpsAndValidity``` - computes truth value of WFF under all interpretations & validity of WFF    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/o3q3zQH.png)

      </details>
      
* ```interpsAndValidity2``` - same as ```interpsAndValidity``` but table view
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/o3q3zQH.png)

      </details>
      
* ```subfInterpsAndValidity``` - computes interpretation for all truth values of all subformulas of a WFF
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/o3q3zQH.png)

      </details>
            
###### Node: programs above depend on ```lcsHelperFunc.py```

# WFF Relaxation
### Connectives
1. ```Negation``` : ```!``` <br/>
2. ```And``` : ```^``` <br/>
3. ```Or``` : ```|``` <br/>
4. ```Implication``` : ```>``` <br/>
5. ```Equivalence``` : ```-```  <br/>
6. ```Atoms possible``` : ```[a-z] & [A-Z]``` <br/>
### Input examples
 ```A|B```  <br/>
 ```A>B|(!C)``` <br/>
 ```(A-B)^(C|!A))>A``` <br/>
 ```A>B|C^D```
#### Programs available
* ```relaxedToStrong``` - convert a formula from relaxed form to strong from
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/o3q3zQH.png)

      </details>
      
* ```convertToNNF``` - convert formula to Negation Normal Form (NNF)
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/o3q3zQH.png)

      </details>
      
* ```convertToCNF``` - convert formula to Conjunctive Normal Form (CNF)
    
    - <details>

      <summary>Example output here</summary>

      ![Imgur Image](https://i.imgur.com/o3q3zQH.png)

      </details>
      
###### Node: programs above depend on ```relHelperFunc.py```



DEPENDS ON: lcs_helper.py ( HELPER CLASS )
  - lcs.py  <=> CHECK IF A FORMULA IS A WFF
  - lcs2.py  <=> GET TRUTH VALUE OF A WFF UNDER A SPECIFIC INTERPRETATION
  - lcs3.py  <=> INTERPRETATION UNDER ALL TRUTH VALUES AND VALIDITY CHECK OF A WFF
  - lcs3_1.py <=> INTERPRETATION UNDER ALL TRUTH VALUES OF A WFF (TABLE VIEW)
  - lcs4.py <=> INTERPRETATION UNDER ALL TRUTH VALUES OF ALL SUBFORMULAS OF A WFF
 
DEPENDS ON: rel_helper.py ( HELPER CLASS )
  - rel.py <=> CONVERTS A FORMULA FROM RELAXED FORM TO STRONG FORM
 
DEPENDS ON: re.py ( HELPER CLASS )
  - n.py <=> CONVERTS A RELAXED/STRONG FORM FORMULA TO NNF

DEPENDS ON: n.py ( HELPER CLASS )
  - c.py <=> CONVERTS A NNF FORMULA TO CNF
 
 DEPENDS ON: nothing
  - cls.py <=> CHECKS IF A CLAUSE SET IF SAT OR UNSAT ( where clauses are in the form: A,B,!B  etc )
