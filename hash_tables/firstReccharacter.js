//finding the first repeating char from the array 

//arr1=[1,2,2,3,4] //returns 2
//arr2==[1,4,5,5,4] //returns 5

//blutal 0(n sqaured) since includes method is actual o(n) and inside a for loop resutlts in o(n sqaured)

// let arr=[1,2,3,3,4]
// function findFirstRecChar(arr){
//     let arr2=[]
//     for(let i=0;i<arr.length;i++){
//          if(arr2.includes(arr[i])){
//             return arr[i]

//         } else{
//             arr2.push(arr[i])
//         }  

//     }
//     return null
    

// }

// console.log(findFirstRecChar([1,6,6,2,3,4,4]))


// working on optimized solution using hash table.... js objects
//beow is o(n) i guess cz of the loop... objs are generally o(1) even though we might have colission that might cz o(n)

let arr=[1,2,2,3,4]
function findFirstRecChar(arr){
    let obj={}
    for(let i=0;arr.length;i++){
        if(arr[i] in obj){
            return arr[i]
        }
        else{
            obj[arr[i]]=true
        }
        
       
    }

    return null
}
console.log(findFirstRecChar([1,6,6,2,3,4,4] ))


