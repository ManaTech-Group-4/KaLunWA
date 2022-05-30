import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IndivEventsModel } from 'src/app/features/models/indiv-event-model';
import { CollectivePageModel } from '../model/collective-page-model';

@Injectable({
  providedIn: 'root'
})
export class CollectivePagesService {

  constructor(private http: HttpClient) { }

  getProjectList(): Observable<CollectivePageModel[]>{
    return this.http.get<any>("http://127.0.0.1:8000/api/projects/?omit=image,updated_at,created_at,description,end_date");
  }
  getEventList(): Observable<CollectivePageModel[]>{
    return this.http.get<any>("http://127.0.0.1:8000/api/events/?omit=image,updated_at,created_at,description,end_date");
  }

  getAnnouncementList(): Observable<CollectivePageModel[]>{
    return this.http.get<any>("http://127.0.0.1:8000/api/announcements/?updated_at,created_at,description,end_date");
  }
  getNewsList(): Observable<CollectivePageModel[]>{
    return this.http.get<any>("http://127.0.0.1:8000/api/news/?omit=image,updated_at,created_at,description,end_date");
  }


  addProject(){
    console.log("project added");
  }
  updateProject(){
    console.log("project updated");
  }

  addEvent(){
    console.log("Event added");
  }
  updateEvent(){
    console.log("Event updated");
  }

  addNews(){
    console.log("News added");
  }
  updateNews(){
    console.log("News updated");
  }


  public uploadImage(fileName:string, image:any) {
    const formData = new FormData();

    formData.append("image", image);
    formData.append("name", fileName);
    console.log(image);
    return this.http.post('http://127.0.0.1:8000/api/gallery/', formData);
  }

  getEventDetails(eventId: string | null) : Observable<IndivEventsModel>{
    let address  = 'http://127.0.0.1:8000/api/events/'+eventId+'/?expand=image,contributors.image,gallery&omit=created_at,updated_at,gallery,contributors';
    return this.http.get<IndivEventsModel>(address);
  }
  getProjectDetails(projectId: string | null) : Observable<IndivEventsModel>{
    let address  = 'http://127.0.0.1:8000/api/projects/'+projectId+'/?expand=image,contributors.image,gallery&omit=created_at,updated_at,gallery,contributors';
    return this.http.get<IndivEventsModel>(address);
  }

  getNewsDetails(projectId: string | null) : Observable<IndivEventsModel>{
    let address  = 'http://127.0.0.1:8000/api/news/'+projectId+'/?expand=image,contributors.image,gallery&omit=created_at,updated_at';
    return this.http.get<IndivEventsModel>(address);
  }


  printDate(date: Date){
    let month = "";
    switch(date.getMonth()){
      case 1:
        month="January";
        break;
      case 2:
        month="February";
        break;
      case 3:
        month="March";
        break;
      case 4:
        month="April";
        break;
      case 5:
        month="May";
        break;
      case 6:
        month="June";
        break;
      case 7:
        month="July";
        break;
      case 8:
        month="August";
        break;
      case 9:
        month="September";
        break;
      case 10:
        month="October";
        break;
      case 11:
        month="November";
        break;
      case 12:
        month="December";
        break;
    }

    return month + " " + date.getDay() + ", " + date.getFullYear();
  }
}
