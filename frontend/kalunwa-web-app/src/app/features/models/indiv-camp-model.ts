import { CampEventModel, CampProjectModel } from "./campReqests/campRequests-model";

export interface IndivCampModel{
  id: number,
  content_image: string,
  content: string,
  gallery: Array<{id:number, image: string, thumbImage: string}>,
  events: Array<CampEventModel>,
  projects: Array<CampProjectModel>
}
