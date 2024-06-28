import { notFound } from "next/navigation";
import type { Metadata } from "next";
// export default function ProductDetails({params}:{params:{productId:string}})

// {
//     return <h1>Product Details:{params.productId}</h1>
// }
// type Props = { params: { productId: string } };

// export const generateMetadata = ({ params }: Props): Metadata => {
//   return {
//     title: `Product ${params.productId}`,
//   };
// };

type Props = {
  params: { productId: string };
};

const generateMetadata = {};

export default function ProductDetails({ params }: Props) {
  if (parseInt(params.productId) > 100) {
    notFound();
  }
  return (
    <>
      <h1>Product Details:{params.productId}</h1>
    </>
  );
}
