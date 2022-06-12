import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ConfirmDialog } from '../dialogs/confirm-dialog/confirm-dialog';

@Injectable({
  providedIn: 'root'
})
export class DialogsService {

  constructor(
    public dialog: MatDialog) { }


}
