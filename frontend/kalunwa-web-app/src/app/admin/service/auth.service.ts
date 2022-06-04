import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Admin } from '../model/user-model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private currentUserSubject: BehaviorSubject<Admin>;
  public currentUser: Observable<Admin>;

  constructor(private http: HttpClient) {
    this.currentUserSubject = new BehaviorSubject<Admin>(JSON.parse(localStorage.getItem('currentUser')!));
    this.currentUser = this.currentUserSubject.asObservable();
  }

  public get currentUserValue(): Admin {
      return this.currentUserSubject.value;
  }


  login(email:string, password:string)
  {
    console.log(email,password);
    return this.http.post<Admin>(`http://127.0.0.1:8000/api/token/`, {email,password})
      .pipe(map(user => {
          // store user details and jwt token in local storage to keep user logged in between page refreshes
          localStorage.setItem('currentUser', JSON.stringify(user));
          this.currentUserSubject.next(user);
          return user;
      }));
  }

  logout() {
    // remove user from local storage and set current user to null
    localStorage.removeItem('currentUser');
    this.currentUserSubject.next(null);
  }

}
