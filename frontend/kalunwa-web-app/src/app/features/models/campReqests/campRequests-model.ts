export interface CampInfoModel{
  id: number,
  name: string,
  description:string,
  image: {id:number, image: string},
  gallery:  Array<{id:number, image: string, thumbImage: string}>
}
export interface CampEventModel{
  id: number,
  image: {id:number, image: string},
  title:string
}
export interface CampProjectModel{
  id: number,
  image: {id:number, image: string},
  title:string
}
