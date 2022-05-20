import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Admin } from '../model/user-model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private currentUserSubject: BehaviorSubject<Admin>;
  public currentUser: Observable<Admin>;

  constructor() {
    // this.currentUserSubject = new BehaviorSubject<Admin>(JSON.parse(localStorage.getItem('user')|| ""));
    // this.currentUser = this.currentUserSubject.asObservable();
  }

  login(username:string, password:string)
  {
    console.log(username,password);
  }
}
