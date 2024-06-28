export default function ReviewId({params}:{params:{productId:string,reviewId:string}}){
    return <>
    <h1>Product ID:{params.productId}</h1>
    <h1>Review ID:{params.reviewId}</h1>
    
    </>
}