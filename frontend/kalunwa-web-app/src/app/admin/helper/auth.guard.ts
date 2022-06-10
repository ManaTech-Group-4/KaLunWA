import { Injectable } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { AuthService } from '../service/auth.service';


@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
    constructor(
        private router: Router,
        private authService: AuthService
    ) {}

    canActivate() {
      if (this.authService.isLoggedIn()) {

        return true;
      } else {
        this.authService.logout();
        this.router.navigate(['login']);

        return false;
      }
    }
}
