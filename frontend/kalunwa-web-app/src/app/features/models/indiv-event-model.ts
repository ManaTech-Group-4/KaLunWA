export interface IndivEventsModel{
  id:number;
  title: string;
  tagline: string;
  cover_image: any;
  start_date:string;
  end_date:string;
  camp: string;
  status: string;
  description: string;
  gallery: Array<any>;
  contributors:Array<any>;
}
