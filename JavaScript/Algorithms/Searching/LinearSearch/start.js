const FANG=["google","amazon","facebook","netflix"]

//write a function that find if the target is among the FANG,  returns its index

//using built in methods
function findIndex(arr,target){
  for(let i=0;i<arr.length;i++){
    if(!arr.includes(target)){
        return null
    }
    else{
        return arr.indexOf(target)
    }

  }
}


//using just for loops...
function findIndex(arr,target){
    for(let i=0;arr.length;i++){
        if(arr[i]==target){
            return i
        }
        else{
            return null
        }
    }

}


console.log(findIndex(["google","amazon","facebook","netflix"],"google"))