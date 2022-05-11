import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { MembersDialogModel } from '../models/members-dialog-model';

import { OrgService } from './org.service';

describe('OrgService', () => {
  let service: OrgService,
      httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports : [HttpClientTestingModule]
    });
    service = TestBed.inject(OrgService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  // it('should retrieve total Demographics', () => {
  //   const testMembers =[
  //     {
  //         "id": 1,
  //         "position": "President",
  //         "first_name": "Jairus",
  //         "last_name": "Chiu",
  //         "quote": "advocacy",
  //         "image": {
  //             "id": 23,
  //             "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
  //         }
  //     },
  //     {
  //         "id": 2,
  //         "position": "Vice-President",
  //         "first_name": "Vice",
  //         "last_name": "Pres",
  //         "quote": "advocacy",
  //         "image": {
  //             "id": 24,
  //             "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
  //         }
  //     },
  //     {
  //         "id": 3,
  //         "position": "Secretary",
  //         "first_name": "Sec",
  //         "last_name": "Retary",
  //         "quote": "advocacy",
  //         "image": {
  //             "id": 25,
  //             "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
  //         }
  //     },
  //     {
  //         "id": 4,
  //         "position": "Treasurer",
  //         "first_name": "Tre",
  //         "last_name": "Asurer",
  //         "quote": "advocacy",
  //         "image": {
  //             "id": 26,
  //             "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
  //         }
  //     },
  //     {
  //         "id": 5,
  //         "position": "Auditor",
  //         "first_name": "Audi",
  //         "last_name": "Tor",
  //         "quote": "advocacy",
  //         "image": {
  //             "id": 27,
  //             "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
  //         }
  //     },
  //     {
  //         "id": 6,
  //         "position": "Director",
  //         "first_name": "ter",
  //         "last_name": "mats",
  //         "quote": "maayong buntag everyday",
  //         "image": {
  //             "id": 18,
  //             "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
  //         }
  //     }
  // ] as MembersDialogModel[];

  //   service.getExec().subscribe((member)=>{
  //     expect(testMembers).toBe(member,'should check mocked data');
  //   });

  //   const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/orgleaders/?expand=image&omit=created_at,updated_at');

  //   expect(req.cancelled).toBeFalsy();
  //   expect(req.request.responseType).toEqual('json');

  //   req.flush(testMembers);

  // });

});
