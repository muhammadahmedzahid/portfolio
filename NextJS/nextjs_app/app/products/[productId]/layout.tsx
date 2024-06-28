import React from "react";

import type { Metadata } from "next";

export const metadata:Metadata = {
    title:"Product page",
    description:"Product description"
}

export default function ProductDetailLayout({children}:{children:React.ReactNode}){
    return (<>
    {children}
    <h1>Product Details Layout</h1>
    </>)
}