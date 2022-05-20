import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { forkJoin, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { CampEventModel, CampInfoModel, CampProjectModel } from '../models/campReqests/campRequests-model';
import { IndivCampModel } from '../models/indiv-camp-model';

@Injectable({
  providedIn: 'root'
})
export class IndivCampService {

  constructor(private http: HttpClient) { }

  //http://127.0.0.1:8000/api/events/?camp=Zero%20Waste&omit=created_at,updated_at,description,status,start_date,end_date,camp
  //http://127.0.0.1:8000/api/camps/1/?expand=gallery&omit=camp_leader,created_at,updated_at
  //http://127.0.0.1:8000/api/projects/?camp=Zero%20Waste&omit=created_at,updated_at,description,status,start_date,end_date,camp

  getIndivCamp(id:number, camp:string): IndivCampModel{
    let newCamp: IndivCampModel = {
      "id": 1,
      "content_image": "assets/images/baybayon.png",
      "content": "",
      "gallery": [],
      "events": [],
      "projects": []
    };
    forkJoin({reqOne: this.getCampInfo(id), reqTwo: this.getCampEvents(camp),reqThree: this.getCampProjects(camp)}).subscribe(
      ({reqOne,reqTwo,reqThree})=>
      {
        newCamp.id = reqOne.id;
        newCamp.content_image = reqOne.image.image;
        newCamp.gallery =  reqOne.gallery;
        newCamp.content = reqOne.description;
        newCamp.events = reqTwo;
        newCamp.projects = reqThree;
        console.log(newCamp);
      }
    );
    return newCamp;
  }

  getCampInfo(id:number){
    let address = "http://127.0.0.1:8000/api/camps/"+id+"/?expand=gallery,image&omit=camp_leader,created_at,updated_at";
    return this.http.get<CampInfoModel>(address);
  }

  getCampEvents(camp:string){
    let address = "http://127.0.0.1:8000/api/events/?expand=image&camp="+camp+"&omit=created_at,updated_at,description,status,start_date,end_date,camp";
    return this.http.get<CampEventModel[]>(address);
  }

  getCampProjects(camp:string){
    let address = "http://127.0.0.1:8000/api/projects/?expand=image&camp="+camp+"&omit=created_at,updated_at,description,status,start_date,end_date,camp";
    return this.http.get<CampProjectModel[]>(address);
  }
}
