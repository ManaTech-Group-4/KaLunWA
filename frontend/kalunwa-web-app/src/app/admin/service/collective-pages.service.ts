import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IndivEventsModel } from 'src/app/features/models/indiv-event-model';
import { AnnoucementModel } from 'src/app/features/models/news-model';
import { CollectivePageModel } from '../model/collective-page-model';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class CollectivePagesService {
  headers = new HttpHeaders({
      'Authorization': `Bearer ${this.auth.access}`
    });

  constructor(private http: HttpClient,private auth: AuthService) { }

  getProjectList(): Observable<CollectivePageModel[]>{
    return this.http.get<any>("http://127.0.0.1:8000/api/projects/?omit=image,updated_at,description,end_date");
  }
  getEventList(): Observable<CollectivePageModel[]>{
    return this.http.get<any>("http://127.0.0.1:8000/api/events/?omit=image,updated_at,description,end_date");
  }

  getAnnouncementList(): Observable<CollectivePageModel[]>{
    return this.http.get<any>("http://127.0.0.1:8000/api/announcements/?updated_at,description,end_date");
  }
  getNewsList(): Observable<CollectivePageModel[]>{
    return this.http.get<any>("http://127.0.0.1:8000/api/news/?omit=image,updated_at,description,end_date");
  }


  addProject(newProject:any){
    return this.http.post(`http://127.0.0.1:8000/api/projects/`, newProject, {headers:this.headers});
  }
  updateProject(upProject:any, id:string | null){
    return this.http.put(`http://127.0.0.1:8000/api/projects/${id}/`, upProject, {headers:this.headers});
  }
  deleteProject(id:number){
    return this.http.delete(`http://127.0.0.1:8000/api/projects/${id}/`, {headers:this.headers});
  }



  addEvent(newEvent:any){
    return this.http.post(`http://127.0.0.1:8000/api/events/`, newEvent, {headers:this.headers});
  }
  updateEvent(upEvent:any, id:string | null){
    return this.http.put(`http://127.0.0.1:8000/api/events/${id}/`, upEvent, {headers:this.headers});
  }
  deleteEvent(id:number){
    return this.http.delete(`http://127.0.0.1:8000/api/events/${id}/`, {headers:this.headers});
  }


  addNews(newNews:any){
    return this.http.post(`http://127.0.0.1:8000/api/news/`, newNews, {headers:this.headers});
  }
  updateNews(upNews:any, id:string | null){
    return this.http.put(`http://127.0.0.1:8000/api/news/${id}/`, upNews, {headers:this.headers});
  }
  deleteNews(id:number){
    return this.http.delete(`http://127.0.0.1:8000/api/news/${id}/`, {headers:this.headers});
  }


  addAnnoucement(newAnnoucements:any){
    return this.http.post(`http://127.0.0.1:8000/api/announcements/`, newAnnoucements, {headers:this.headers});
  }
  updateAnnoucement(upAnnouncement:any, id:string | null){
    return this.http.put(`http://127.0.0.1:8000/api/announcements/${id}/`, upAnnouncement, {headers:this.headers});
  }
  deleteAnnouncement(id:number){
    return this.http.delete(`http://127.0.0.1:8000/api/announcements/${id}/`, {headers:this.headers});
  }


  public uploadImage(fileName:string, image:any) {
    const formData = new FormData();
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.auth.access}`
    });

    formData.append("image", image);
    formData.append("name", fileName);
    console.log(image);
    return this.http.post('http://127.0.0.1:8000/api/gallery/', formData, {headers: headers});
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

  getAnnoucement(annoucementId: string | null) : Observable<AnnoucementModel>{
    return this.http.get<AnnoucementModel>(`http://127.0.0.1:8000/api/announcements/${annoucementId}/?omit=updated_at,last_updated_by`);
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
