export interface IndivEventsModel{
  id:number;
  title: string;
  image: {id: number, image: string};
  start_date:string;
  end_date:string;
  camp: string;
  status: string;
  description: string;
  gallery: Array<{id: number, image: string, thumbImage: string}>;
  contributors:Array<any>;
}
