import { HttpClient, HttpEvent, HttpHandler, HttpHeaders, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { map, shareReplay, tap } from 'rxjs/operators';
import { Admin, Profile, ProfileReceive} from '../model/user-model';
import * as jwtDecode from 'jwt-decode';
import * as moment from 'moment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) {
  }


  get refresh(): string {
    return localStorage.getItem('refresh')!;
  }
  get access(): string {
    return localStorage.getItem('access')!;
  }


  private setSession(authResult:any) {
    const payload = <Admin> jwtDecode.default(authResult.access);
    const expiresAt = moment.unix(payload.exp);

    localStorage.setItem('access', authResult.access);
    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf()));
  }


  login(email:string, password:string)
  {
    return this.http.post(`http://127.0.0.1:8000/api/token/`, {email,password})
      .pipe(
        tap((response:any) => {this.setSession(response);
                              localStorage.setItem('refresh', response.refresh);
                      }),
        shareReplay(),
      );
  }

  logout() {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${this.access}`
    });
    return this.http.post(`http://127.0.0.1:8000/api/users/logout/blacklist/`,{refresh: this.refresh}, {headers: headers}).pipe(
      tap(() => {
        localStorage.removeItem('refresh');
        localStorage.removeItem('access');
        localStorage.removeItem('expires_at');
      })
    )
  }


  register(newAdmin: FormData){
    console.log(newAdmin);
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.access}`
    });

    return this.http.post(`http://127.0.0.1:8000/api/users/register/`, newAdmin, { headers: headers });
  }

  updateUser(updateAdmin: FormData, id:string|null){
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.access}`
    });

    return this.http.put(`http://127.0.0.1:8000/api/users/${id}/`, updateAdmin, { headers: headers });
  }


  delete(id:number){
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.access}`
    });

    return this.http.delete(`http://127.0.0.1:8000/api/users/${id}/`, { headers: headers });
  }



  // refreshToken() {
  //   if (moment().isBetween(this.getExpiration().subtract(1, 'days'), this.getExpiration())) {
  //     return this.http.post(
  //       `http://127.0.0.1:8000/api/token/refresh/`,
  //       { refresh: this.refresh}
  //     ).pipe(
  //       tap(response => this.setSession(response)),
  //       shareReplay(),
  //     ).subscribe();
  //   }
  // }

  getExpiration() {
    const expiration = localStorage.getItem('expires_at');
    const expiresAt = JSON.parse(expiration!);

    return moment(expiresAt);
  }

  get currentAdmin(): Admin{
    const jwtToken = <Admin> jwtDecode.default(localStorage.getItem('access')!);
    return jwtToken;
  }


  isLoggedIn() {
    return moment().isBefore(this.getExpiration());
  }

  isLoggedOut() {
    return !this.isLoggedIn();
  }

  getUsers(){
    return this.http.get<ProfileReceive[]>(`http://127.0.0.1:8000/api/users`,{headers: {'Authorization':  `Bearer ${this.access}`}});
  }

  getUserById(id:string | null){
    return this.http.get<ProfileReceive>(`http://127.0.0.1:8000/api/users/${id}/`,{headers: {'Authorization':  `Bearer ${this.access}`}});
  }

}
