// arr=[1,3,4,67,87,23,68,8]

//write a function that would sort an array in ascending order

function sortAsc(arr){
let sorted=arr.sort(function checkNumbers(a,b){
    return a-b
})
return sorted
    
}
//testing
// console.log(sortAsc([1,3,4,67,87,23,68,8]))

//write a function that would sort an array in descending order

function sortDesc(arr){
    let sorted=arr.sort(function checkNumbers(a,b){
        return b-a
    })
    return sorted
}
// console.log(sortDesc([1,3,4,67,87,23,68,8]))