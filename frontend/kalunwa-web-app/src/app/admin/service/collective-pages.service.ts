import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
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
  getNewsList(): Observable<CollectivePageModel[]>{
    return this.http.get<any>("http://127.0.0.1:8000/api/news/?omit=image,updated_at,created_at,description,end_date");
  }
}
