//write a function that finds the factorial of any number. one should use recursive, the other should just use a for loop


function findFactRec(number){

if(number==0 ||number==1){
    return 1
}
else{
    return number*findFactRec(number-1)
}
}

console.log(findFactRec(2))



function findFactLoop(number){
    //5!=5*(5-1).....*1
    let ans=1
 for(let i=1;i<=number;i++){
    ans=ans*i //ans=1*1*2*3*4*5
 }
 return ans

}
console.log(findFactLoop(5))